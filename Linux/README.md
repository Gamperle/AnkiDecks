# Linux Anki Decks

Flashcard decks covering Linux fundamentals, system administration, and kernel internals — classified by difficulty level.

## Format

```
Front (question or term)[TAB]Back (answer or definition)
```

---

## Available Decks

| File | Description |
|------|-------------|
| `linux_beginner.txt` | Shell basics, filesystem, permissions, users, package management, processes |
| `linux_intermediate.txt` | Systemd, networking, storage, scripting, containers, monitoring, security hardening |
| `linux_pro.txt` | Kernel internals, namespaces/cgroups, performance tuning, eBPF, boot process, custom kernels |

---

## Topic Index

### Beginner

#### 1. Shell & Command Line Basics
- Shells: bash, zsh, sh — differences and defaults
- Command structure: command, arguments, options (-v, --verbose)
- Path: absolute vs relative, . and .. and ~
- Man pages, --help, info, tldr
- Command chaining: ;, &&, ||, pipes (|), redirection (>, >>, 2>, &>)
- Environment variables: $PATH, $HOME, $USER, export
- Quoting: single quotes, double quotes, escape characters
- Globbing: *, ?, [], {}
- History: history, !!, !n, Ctrl+R

#### 2. Filesystem & Navigation
- FHS (Filesystem Hierarchy Standard): /, /bin, /etc, /home, /var, /tmp, /usr, /opt, /proc, /sys, /dev
- Navigation: cd, pwd, ls, tree
- File operations: cp, mv, rm, mkdir, touch, ln (hard/soft links)
- File inspection: cat, less, more, head, tail, wc, file
- Searching: find, locate, which, whereis
- Text processing: grep, sed, awk, cut, sort, uniq, tr, xargs

#### 3. Users, Groups & Permissions
- Users: /etc/passwd, /etc/shadow, useradd, usermod, userdel, passwd
- Groups: /etc/group, groupadd, usermod -aG
- File permissions: rwx, owner/group/other, chmod (symbolic and octal)
- chown, chgrp
- Special bits: setuid, setgid, sticky bit
- umask: default permission mask
- sudo and /etc/sudoers, visudo

#### 4. Package Management
- Debian/Ubuntu: apt, apt-get, dpkg, .deb packages
- Red Hat/Fedora: dnf, yum, rpm, .rpm packages
- Arch: pacman
- Universal: snap, flatpak, AppImage
- Repository management, GPG key verification
- Building from source: configure, make, make install

#### 5. Processes & Job Control
- Processes: PID, PPID, process states (R, S, D, Z, T)
- ps, top, htop, pgrep, pidof
- Signals: kill, SIGTERM, SIGKILL, SIGHUP, SIGINT, SIGSTOP
- Job control: &, fg, bg, jobs, Ctrl+Z, Ctrl+C
- nohup, disown, screen, tmux
- /proc filesystem: /proc/PID/status, /proc/cpuinfo, /proc/meminfo
- Zombie processes: what they are and how to clean them up

#### 6. Basic Networking
- ip addr, ip route, ip link (replacing ifconfig, route)
- Hostname, DNS resolution: /etc/hosts, /etc/resolv.conf, dig, nslookup
- ping, traceroute, mtr
- ss, netstat — viewing connections and listening ports
- curl, wget — fetching URLs
- SSH basics: ssh, ssh-keygen, ssh-copy-id, ~/.ssh/config, authorized_keys

---

### Intermediate

#### 7. Systemd & Service Management
- systemd architecture: unit files, targets, timers, sockets
- systemctl: start, stop, enable, disable, status, restart, daemon-reload
- Unit file structure: [Unit], [Service], [Install] sections
- Service types: simple, forking, oneshot, notify, idle
- journalctl: log querying, filtering by unit/time/priority
- Timers as cron replacement: .timer and .service pairs
- Socket activation: on-demand service startup
- systemd-analyze: boot time analysis, blame, critical-chain

#### 8. Networking & Firewalls
- Network configuration: /etc/netplan, /etc/network/interfaces, NetworkManager, systemd-networkd
- iptables: tables, chains (INPUT, OUTPUT, FORWARD), rules, targets (ACCEPT, DROP, REJECT)
- nftables: replacing iptables, nft command, rule syntax
- ufw — simplified firewall management
- firewalld and zones
- NAT, port forwarding, masquerading
- Network troubleshooting: tcpdump, wireshark, nmap
- VPN basics: WireGuard, OpenVPN
- DNS server basics: systemd-resolved, dnsmasq, BIND overview

#### 9. Storage & Filesystems
- Block devices: /dev/sda, /dev/nvme0n1, lsblk
- Partitioning: fdisk, gdisk, parted, MBR vs GPT
- Filesystems: ext4, XFS, Btrfs, ZFS — features and trade-offs
- Mounting: mount, /etc/fstab, UUID vs device path, mount options
- LVM: PV, VG, LV — creating, extending, snapshots
- RAID: levels 0, 1, 5, 6, 10 — mdadm
- Swap: swap partition, swap file, swappiness
- Disk monitoring: df, du, iostat, iotop, smartctl

#### 10. Shell Scripting
- Shebang: #!/bin/bash, #!/usr/bin/env bash
- Variables, arrays, associative arrays
- Conditionals: if/elif/else, [[ ]], test, -f, -d, -z, -n, -eq, -lt
- Loops: for, while, until, break, continue
- Functions: definition, arguments ($1, $2, $@, $#), return values
- String manipulation: ${var#pattern}, ${var%pattern}, ${var/old/new}
- Exit codes: $?, set -e, set -o pipefail, trap
- Heredocs and here-strings
- Process substitution: <(command), >(command)

#### 11. Containers & Virtualization
- Containers vs VMs — kernel sharing, isolation differences
- Docker basics: images, containers, Dockerfile, docker build, docker run
- Docker networking: bridge, host, overlay
- Docker volumes and bind mounts
- Docker Compose: multi-container orchestration
- Podman: daemonless containers, rootless mode
- OCI standards: image spec, runtime spec
- KVM/QEMU basics: libvirt, virsh, virt-manager
- Systemd-nspawn: lightweight containers

#### 12. Monitoring & Logging
- System logs: journalctl, /var/log/syslog, /var/log/messages, /var/log/auth.log
- Syslog protocol, rsyslog, syslog-ng
- Log rotation: logrotate configuration
- System monitoring: top, htop, vmstat, sar, dstat
- Memory monitoring: free, /proc/meminfo, slabtop
- Disk I/O monitoring: iostat, iotop, blktrace
- Network monitoring: iftop, nethogs, bmon, vnstat
- Uptime, load average: what 1/5/15 minute values mean

#### 13. Security Hardening
- SSH hardening: disable root login, key-only auth, port change, fail2ban
- SELinux: modes, contexts, booleans, troubleshooting (audit2why)
- AppArmor: profiles, enforce vs complain mode
- File integrity: AIDE, Tripwire
- Auditd: system call auditing, audit rules, ausearch
- PAM (Pluggable Authentication Modules): authentication stack
- Disk encryption: LUKS, dm-crypt
- Kernel security modules: seccomp, capabilities, namespaces

---

### Pro

#### 14. Kernel Fundamentals
- Linux kernel architecture: monolithic kernel with loadable modules
- Kernel space vs user space, system calls as the boundary
- Process management: task_struct, process states, context switching
- Scheduler: CFS (Completely Fair Scheduler), priorities, nice values, RT scheduling
- Memory management: virtual memory, page tables, TLB, page faults, copy-on-write
- Kernel memory: slab allocator, kmalloc, vmalloc, buddy system
- VFS (Virtual Filesystem Switch): inode, dentry, superblock, file operations
- Interrupt handling: top-half and bottom-half (softirq, tasklet, workqueue)
- Character devices, block devices, device drivers overview

#### 15. Namespaces & Cgroups
- Linux namespaces: PID, net, mnt, uts, ipc, user, cgroup, time
- Creating namespaces: unshare, nsenter, clone() with CLONE_NEW*
- PID namespace: PID 1 inside container, PID isolation
- Network namespace: virtual interfaces, veth pairs, network isolation
- Mount namespace: isolated filesystem views, pivot_root
- User namespace: UID mapping, rootless containers
- Cgroups v1 vs v2: hierarchy, controllers, unified vs split
- Cgroup controllers: cpu, memory, io, pids, cpuset
- Memory cgroup: limits, OOM killer, memory.max, memory.swap.max
- CPU cgroup: cpu.max (bandwidth limiting), cpu.weight (shares)
- Systemd integration: systemd slices, scopes, per-service resource controls

#### 16. Performance Tuning
- Performance analysis methodology: USE method (Utilization, Saturation, Errors)
- CPU tuning: cpufreq governors, CPU pinning (taskset, isolcpus), NUMA awareness
- Memory tuning: vm.swappiness, huge pages (THP, hugetlbfs), vm.dirty_ratio, vm.overcommit_memory
- I/O tuning: I/O schedulers (mq-deadline, bfq, none/noop), direct I/O, readahead
- Network tuning: TCP buffer sizes, socket buffers, congestion control algorithms (BBR, CUBIC), SO_REUSEPORT
- Filesystem tuning: mount options (noatime, discard), journal modes, block size
- perf tool: stat, record, report, flame graphs
- strace: tracing system calls and signals
- ltrace: tracing library calls
- /proc and /sys tuning: sysctl, /sys/class, /sys/kernel

#### 17. eBPF & Observability
- What is eBPF: in-kernel virtual machine for programmable tracing, networking, and security
- BPF programs: types (kprobe, tracepoint, XDP, cgroup, socket)
- BCC (BPF Compiler Collection): Python-based tools (execsnoop, biolatency, tcplife)
- bpftrace: high-level tracing language, one-liners, probes
- eBPF maps: hash maps, arrays, ring buffers for kernel-user communication
- XDP (eXpress Data Path): programmable packet processing at NIC driver level
- eBPF verifier: safety guarantees, bounded loops, memory access checks
- eBPF for security: Seccomp-BPF, Cilium, Falco
- BPF Type Format (BTF): portable eBPF programs across kernel versions (CO-RE)

#### 18. Boot Process & Init
- BIOS/UEFI → bootloader → kernel → init → userspace
- UEFI: Secure Boot, EFI System Partition (ESP), UEFI variables
- GRUB2: configuration, grub.cfg, grub-mkconfig, kernel parameters
- Kernel boot: decompression, start_kernel(), init_task, initramfs/initrd
- initramfs: purpose, contents, dracut vs mkinitramfs
- PID 1 (init): systemd, OpenRC, runit, s6 — responsibilities and differences
- systemd boot targets: multi-user.target, graphical.target, rescue.target, emergency.target
- Kernel command line parameters: root=, init=, quiet, verbose, single

#### 19. Custom Kernels & Modules
- Kernel configuration: make menuconfig, .config file, CONFIG_ options
- Building the kernel: make, make modules, make modules_install, make install
- Kernel modules: .ko files, insmod, rmmod, modprobe, lsmod
- depmod: module dependency resolution
- DKMS: Dynamic Kernel Module Support for out-of-tree modules
- Writing a basic kernel module: module_init, module_exit, MODULE_LICENSE
- /proc and /sys entries: creating custom interfaces
- Device drivers: character device registration, file_operations, major/minor numbers
- Kernel debugging: printk, dmesg, ftrace, kgdb, crash utility
