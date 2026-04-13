from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.recoco import Timer
import time

log = core.getLogger()

prev_stats = {}

# When switch connects
def _handle_ConnectionUp(event):
    log.info("Switch %s connected", event.connection)

# Request stats periodically
def request_stats():
    for connection in core.openflow._connections.values():
        connection.send(of.ofp_stats_request(
            body=of.ofp_port_stats_request()
        ))

# Handle port stats
def _handle_PortStatsReceived(event):
    global prev_stats

    for stat in event.stats:
        # Ignore LOCAL port
        if stat.port_no == 65534:
            continue

        port = stat.port_no
        key = (event.connection.dpid, port)

        current_bytes = stat.tx_bytes + stat.rx_bytes

        if key in prev_stats:
            prev_bytes, prev_time = prev_stats[key]
            now = time.time()

            time_diff = now - prev_time
            byte_diff = current_bytes - prev_bytes

            if time_diff > 0:
                # Bytes/sec → Mbps
                bandwidth = byte_diff / time_diff
                bandwidth_mbps = (bandwidth * 8) / (10**6)

                # Assume link capacity = 1000 Mbps
                link_capacity = 1000
                utilization = (bandwidth_mbps / link_capacity) * 100

                log.info("Port %s -> Bandwidth: %.2f Mbps | Utilization: %.2f%%",
                         port, bandwidth_mbps, utilization)

        prev_stats[key] = (current_bytes, time.time())

# Handle packets + install flow rules
def _handle_PacketIn(event):
    packet = event.parsed
    in_port = event.port

    # Install flow rule (match-action)
    flow_mod = of.ofp_flow_mod()
    flow_mod.match = of.ofp_match.from_packet(packet, in_port)

    # Action: flood (basic forwarding)
    flow_mod.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))

    # Optional: set timeout
    flow_mod.idle_timeout = 30
    flow_mod.hard_timeout = 60

    event.connection.send(flow_mod)

    # Also send current packet
    packet_out = of.ofp_packet_out()
    packet_out.data = event.ofp
    packet_out.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    event.connection.send(packet_out)

def launch():
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
    core.openflow.addListenerByName("PortStatsReceived", _handle_PortStatsReceived)
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)

    # Request stats every 2 seconds
    Timer(2, request_stats, recurring=True)

    log.info("✅ Final Bandwidth Monitor with Flow Rules Started 🚀")
