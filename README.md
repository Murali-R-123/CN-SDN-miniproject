# 📊 Network Utilization Monitor (SDN Project)

## 🧠 Overview

This project implements a **Network Utilization Monitor** using **Software Defined Networking (SDN)** concepts. It measures and displays bandwidth usage across the network in real time.

The system collects flow statistics from switches, estimates bandwidth consumption, and periodically updates the utilization for monitoring purposes.

---

## 🎯 Objectives

* Measure network traffic using byte counters
* Estimate bandwidth utilization between hosts
* Display network usage dynamically
* Update statistics periodically

---

## 🏗️ Technologies Used

* **Mininet** – Network emulation
* **POX Controller** – SDN controller
* **Open vSwitch (OVS)** – Virtual switch
* **Python** – Backend logic and controller implementation

---

## ⚙️ Project Setup

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

## 🔍 How It Works

1. Hosts generate traffic in the Mininet topology
2. Switches maintain flow statistics (packet count, byte count)
3. The controller collects these statistics
4. Bandwidth utilization is calculated using byte differences over time
5. Results are displayed and updated periodically

---

## 📈 Output

* Displays bandwidth usage between hosts
* Shows packet and byte counts
* Helps analyze network performance

---

## 📂 Project Structure

```
CN SDN miniproject/
│── pox/                     # POX controller files
│── scripts/                 # Monitoring scripts (if any)
│── Output Screenshots/      # Screenshots of results
│── README.md                # Project documentation
```

---

## 🚀 Future Improvements

* Add graphical visualization of network usage
* Implement real-time dashboard
* Extend to larger and complex topologies
* Integrate alert system for high traffic

---

## 👨‍💻 Author

**R Muralidharan**

---

## 📌 Conclusion

This project demonstrates how SDN can be used to monitor and analyze network utilization efficiently by leveraging centralized control and real-time statistics.

---
