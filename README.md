# Task 1

## Build Instructions

The execeution permision is given by defould but if that were to change you can use `chmod +x number.sh` to give execution permision to script before running.
To make script avaliable on all system add it nex to shared binaries, it is usualy at `/usr/local/bin/` but you can use location of you chosing under **$PATH** variable.

The execution permission is given by default but if that were to change you can use `chmod +x number.sh` to give execution permission to script before running. To make script available on all system add it next to shared binaries, it is usually at `/usr/local/bin/` but you can use the location of your choosing under **$PATH** variable.

Example commands;
```
chmod a+x number.sh
cp numbers.sh /usr/local/bin/ 
```

## Usage

If the script is moved/copied under a location in $PATH then simply run the number command. 
If you simply want to run the script run ./number.sh or bash number.sh.


## Description 

number.sh simply generates and array from numbers 1 to 10 and shuffles them using the shuf function and prints them randomly. Each number appears once.

## Known limitations / Bugs

- Relative path for the shuf function is used, depending on the system $PATH variable first binary with the name will be user and this could cause security concerns.
- **shuf** function might not be available on all unix systems.



# Task 2

## What metrics should be monitored

Ram usage metrics to monitor load on device and its health. If RAM is overly used on system the traffic might not pass through.<br />
Disk usage metrics should be monitored to keep track of if the system's disk is full, logs or similar data should be sent to centralized systems if needed and to keep track of disk health.<br /><br />
Disk input/output writing speed metrics to monitor health of disks used.<br />
NIC load metrics to check if the load is saturating the network.<br />
Request return codes such as error, denied or accepted these values can be an indication of cyber attacks. Also requests per client can be an indicator for this as well.<br />
Request rate to determine traffic increase or decrease.<br />
Requests latency time to check if there is a problem either at the backend applications or SSL offloading system. <br />
NIC request numbers per second and source ips, this gives both statistical data on systems usage that can be used in various ways and if the system will require scaling.<br />
NIC input/output transferred data, this value should never reach 10Gbit on each NIC or the line becomes saturated.<br />
CPU temperature and load on average of cores and each core if the CPU is healthy.<br />
CPU nice values of process, if any of them is running in a level it should be.<br />
CPU input/output time and idle wait time to check if the CPU is waiting for other hardware components or is it taking time to answer.<br />
SSL certificates themselves should be periodically tested and encryption types, expirations dates should be checked.<br />
Proxy service health should be monitored using monit or similar tools that could take action if it is down.<br />
Open ports of the system should be monitored and only allowed proxy ports should be opened.<br /><br />
Metrics should be monitored using agent like Zabbix or Prometheus to get detailed information from the system. <br />
Metrics mentioned above should be virtualized on a dashboard like Garafana for easier understanding and alerting systems should be placed depending on thresholds defined to notify contact persons.<br />

## Challenges of monitoring the system
If the agent used for monitoring does not support the system used for SSL offloading then SNMP data could be used but that functionality might also not be available for some systems.<br />
If SNMP is also not available on the system that needs to be monitored, that custom script should be written but the process load that the script will create should also be considered and tested before deploying on such solutions.<br />
The compatibility of hardware and software. If the installed operating system is not compatible with the hardware it is installed on then you might not get the metrics you need in order to monitor the system.



