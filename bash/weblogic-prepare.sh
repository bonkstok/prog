#!/bin/bash
read -p "Enter password for oracle user: " passoracle
yum groupinstall "X Window System" -y
yum install unzip -y
yum install nfs-utils -y

mkdir java /usr/java 
unzip java.tar -d /usr/java

mkdir -p /app/oracle/config/domains/mydomain
mkdir -p /app/oracle/product/12.1.1/wlserver


echo "export JAVA_HOME=/usr/java/jdk1.8.0_131" >>/etc/profile #parent of bin ">> /etc/profile
source /etc/profile


mount 192.168.242.169:/nfs/share /mnt

groupadd dba
useradd -g dba oracle
echo "oracle:$passoracle" | chpasswd


echo -e "export ORACLE_BASE=/app/oracle" >> /home/oracle/.bash_profile
echo -e "export ORACLE_HOME=\$ORACLE_HOME/product/12.1.2" >> /home/oracle/.bash_profile
echo -e "export MW_HOME=\$ORACLE_HOME" >> /home/oracle/.bash_profile 
echo -e "export WLS_HOME=\$MW_HOME/wlserver" >> /home/oracle/.bash_profile
echo -e "export WL_HOME=\$WLS_HOME" >> /home/oracle/.bash_profile
echo -e "export DOMAIN_BASE=\$ORACLE_BASE/config/domains" >> /home/oracle/.bash_profile
echo -e "export DOMAIN_HOME=\$DOMAIN_BASE/mydomain" >> /home/oracle/.bash_profile

unzip /mnt/fmw_12.2.1.2.0_wls_Disk1_1of1.zip -d /tmp/
tar -xvf /mnt/jdk-8u131-linux-x64.tar.gz -C /usr/java
