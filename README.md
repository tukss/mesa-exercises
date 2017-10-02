# Stellar structure and evolution (MESA lab course)
Accompanying the lecture on *Advanced Astrophysics* (Stellar structure and evolution) this lab course gives an introduction the software package *Modules for Experimentation in Stellar Astrophysics* (MESA). MESA is a research-grade tool widely used in modelling many aspects of stars.

## Setting up MESA
MESA is a modularised software package mainly written in the language Fortran. As it is common for most simulation codes in science, in particular astrophysics, is is designed to run in a Unix environment and be controlled from the command line. There are many ways of running MESA, either locally on your own machine or on a remote server.

You are not expected to read or modify any of the Fortran code, although you are welcome to have a look.

### Logging into the school's MESA server
We are running a GNU/Linux server with a full install of MESA and many other utilities. Its host name is `phy-mesa01.ncl.ac.uk` and it is currently only reachable from the university network (including Wifi). You can log in remotely either with a pure command-line interface or running a graphical desktop environment. You can use the desktop machines in the cluster or you own device. As the steps for this differ between the different operating systems, please find the instructions in applicable section below.

#### GNU/Linux
You can log in via SSH (secure shell).
You are most likely to have an terminal emulator already installed on your system. Look for programs named Terminal, Konsole or xterm. Start it and type in the following command (replacing username with the name of your university account)
```bash
ssh -Y username@phy-mesa01.ncl.ac.uk
```
When asked to verify the keys compare them with [this section](#ssh-host-keys).

The `-Y` option enables forwarding of all opened windows to your local machine.


#### macOS
You can log in via SSH (secure shell).
Being a Unix system macOS comes with a terminal emulator. To be able to see the graphical output of MESA you need to install an X-server as well. You can download it from [this site](https://www.xquartz.org/).

Start the Terminal app and type in the following command (replacing username with the name of your university account)
```bash
ssh -Y username@phy-mesa01.ncl.ac.uk
```
When asked to verify the keys compare them with [this section](#ssh-host-keys).

The `-Y` option enables forwarding of all opened windows to your local machine.

#### Windows
The school's Windows desktops have the **NX client** installed with which you can log in to a desktop session on the server.

#### Accessing your data
Your have access to your Windows profile directory from the server. Just navigate to the path `/campus/username` (using your login instead of username). Files copied there will be immediately accessible on the university Windows system.

### Installing MESA on your own computer
You can run MESA on your own computer. It should have at least 8 GB of RAM and 10 GB of free disk space.

#### GNU/Linux
- Download MESA SDK from [here](http://www.astro.wisc.edu/%7Etownsend/static.php?ref=mesasdk), install the additional packages mentioned in the package and unpack somewhere in your home directory.
- Open a terminal and run the following commands:

```bash
export MESASDK_ROOT=~/mesasdk
source $MESASDK_ROOT/bin/mesasdk_init.sh
export MESA_DIR=$HOME/path/to/mesa-r10000
cd $MESA_DIR
./install
```
(replace `path/to` accordingly)


#### macOS
- Install Xcode from the app store.
- Run `xcode-select --install` in a terminal.
- Download and install an X-server from https://www.xquartz.org/.
- Download MESA SDK from [here](http://www.astro.wisc.edu/%7Etownsend/static.php?ref=mesasdk) and install it to the Applications folder.
- Download the right release of MESA from http://sourceforge.net/projects/mesa/files/releases/mesa-r10000.zip/download and unpack it somewhere in your home directory.
- Open a terminal and run the commands:

```bash
export MESASDK_ROOT=/Applications/mesasdk
source $MESASDK_ROOT/bin/mesasdk_init.sh
export MESA_DIR=$HOME/path/to/mesa-r10000
cd $MESA_DIR
./install
```
(replace `path/to` accordingly)

#### Windows
While it is possible to install MESA on Windows, we recommend you remotely use the provided Linux server instead. It is quite complicated to get MESA to run properly on a Windows system. If you still want to try it, here is a few possible options.
- Use **cygwin** a Unix environment for Windows.
- Run a Linux distribution in a virtual machine (e.g., using (**VirtualBox**).
- Run MESA in a **Docker** container: https://github.com/evbauer/MESA-Docker

## Running MESA

# SSH host keys
On first login to our server SSH asks you to verify the host key of the server. This is done to prevent someone else tampering with the connection and stealing your password. The key is stored for subsequent logins. Depending on your version of SSH the will be in one of the forms stated below.

```
256 MD5:ec:32:b3:bd:ec:ee:5a:7b:a7:d7:6d:df:3e:43:76:e2 root@phy-mesa01 (ECDSA)
256 MD5:06:57:f9:69:d6:83:b0:4b:c7:76:5a:29:79:4b:f5:11 root@phy-mesa01 (ED25519)
2048 MD5:20:90:5a:a6:f6:ee:c8:3a:af:40:76:f0:21:73:ea:a8 root@phy-mesa01 (RSA)
```

```
256 SHA256:k6ccPTVji3Cp6J6UGLyBScflbeed7gZAUoeIfUcCcV0 root@phy-mesa01 (ECDSA)
256 SHA256:A3nx1bBxWd+oTFtgjQxvAc8fJ5cAKDlXsouPFpZ1LCc root@phy-mesa01 (ED25519)
2048 SHA256:wnDwtQSIiGp5biirrkxSey8rGOEtCIG4ijlkSCbNZEk root@phy-mesa01 (RSA)
```
