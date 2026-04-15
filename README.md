#  Network Utilization Monitor (SDN Project)

##  Overview

This project implements a **Network Utilization Monitor** using **Software Defined Networking (SDN)** concepts. It measures and displays bandwidth usage across the network in real time.

The system collects flow statistics from switches, estimates bandwidth consumption, and periodically updates the utilization for monitoring purposes.

---

##  Objectives

* Measure network traffic using byte counters
* Estimate bandwidth utilization between hosts
* Display network usage dynamically
* Update statistics periodically

---

##  Technologies Used

* **Mininet** – Network emulation
* **POX Controller** – SDN controller
* **Open vSwitch (OVS)** – Virtual switch
* **Python** – Backend logic and controller implementation

## Network Topology

<img width="563" height="459" alt="image" src="https://github.com/user-attachments/assets/d780ad5e-a87b-4e13-9191-f2c03aa4cfd0" />


##  Description

* POX Controller manages the network using OpenFlow

* Switch (s1) connects all hosts

* Hosts (h1, h2, h3) generate traffic

* Communication between controller and switch uses TCP port 6633

---

##  Project Setup

### 1. Start Mininet Topology

```bash
sudo mn --topo single,3 --controller remote --switch ovsk
```

---

### 2. Run POX Controller

```bash
cd pox
./pox.py forwarding.l2_learning
```

---

### 3. Monitor Flow Statistics

```bash
sudo ovs-ofctl dump-flows s1
```

---

##  How It Works

1. Hosts generate traffic in the Mininet topology
2. Switches maintain flow statistics (packet count, byte count)
3. The controller collects these statistics
4. Bandwidth utilization is calculated using byte differences over time
5. Results are displayed and updated periodically

---

## Project Structure

```
CN SDN miniproject/
│── pox/                     # POX controller files
│── scripts/                 # Monitoring scripts (if any)
│── Output Screenshots/      # Screenshots of results
│── README.md                # Project documentation
```
## 📸 Proof of Execution

The following screenshots/logs demonstrate the correct functioning of the SDN Network Utilization Monitor.

### 🔹 Flow Table Entries
The flow table of the OpenFlow switch (s1) was verified using:

sudo ovs-ofctl dump-flows s1

<img width="1207" height="621" alt="image" src="https://github.com/user-attachments/assets/ff7a5e1a-357d-4b7c-a791-88e775313d03" />

This confirms:
- Flow rules are successfully installed by the controller
- Match–action logic is implemented using OpenFlow
- Different protocol flows (ARP, ICMP, IPv6) are handled

---

### 🔹 Ping Test (Low Traffic Scenario)

Command used:
mininet> h1 ping h2

<img width="979" height="377" alt="image" src="https://github.com/user-attachments/assets/54381bf0-5f01-4e74-896a-58cc87fdabce" />

Observed Results:
- 0% packet loss
- Average latency ≈ 4 ms

This demonstrates:
- Basic connectivity between hosts
- Low traffic scenario with minimal bandwidth usage

---

### 🔹 Iperf Test (High Traffic Scenario)

<img width="1127" height="518" alt="image" src="https://github.com/user-attachments/assets/978be8d9-c3a0-4f90-acde-fad40a37ad11" />

Commands used:
mininet> h2 iperf -s &
mininet> h1 iperf -c h2 -t 20

<img width="1005" height="313" alt="image" src="https://github.com/user-attachments/assets/152318b7-9dde-44b2-a5e4-599f8310f017" />


Observed Results:
- Bandwidth ≈ 60–150 Mbps

This demonstrates:
- High traffic generation in the network
- Proper data transfer between hosts

---

### 🔹 Controller Output (Bandwidth & Utilization)

The POX controller logs display:

Port X -> Bandwidth: XX Mbps | Utilization: XX%

<img width="1101" height="493" alt="image" src="https://github.com/user-attachments/assets/0ae8986d-9e73-4911-a3cf-32f15c6a957e" />

This confirms:
- Bandwidth is calculated using byte statistics
- Utilization is computed relative to link capacity (1 Gbps)
- Network usage is monitored in real time

---

### Summary

The above results confirm:
- Successful SDN controller operation
- Accurate bandwidth and utilization monitoring
- Proper handling of both low and high traffic scenarios
- Correct installation of OpenFlow flow rules

---

## Future Improvements

* Add graphical visualization of network usage
* Implement real-time dashboard
* Extend to larger and complex topologies
* Integrate alert system for high traffic

---

##  Author

**R Muralidharan**

---

##  Conclusion

This project demonstrates how SDN can be used to monitor and analyze network utilization efficiently by leveraging centralized control and real-time statistics.

---
