Setting up a Development Environment
====================================

This is something that I end up having to do waaaaaay too often, so I am going to document the process in the order that I did it with the hopes that one day, I will be able to spin these up faster.

Part 1: Creating a Virtual Machine
----------------------------------

We are going to start this process under the assumption that our target environment is going a Virtual Machine running CentOS7.

We start by downloading the Centos 7 minimal install ISO, booting Oracle VM VirtualBox Manager and creating a new VM with that base install running.

### Configuring the Network ###

in `/etc/sysconfig/network` add the line:
> NETWORKING=yes

and make sure that `/etc/sysconfig/network-scripts/ifcfg-<your_device>` has:
> ONBOOT=yes

You can find your device name with `ifconfig` which can be installed with `sudo yum install net-tools.x86_64`

### Install basic packages ###

Run:

> $ `sudo yum update`
> $ `sudo yum install -y wget mlocate tmux`
> $ `sudo yum groupinstall -y "X Window System"`
> $ `sudo yum install -y terminus-fonts`
> $ `sudo yum groupinstall -y "Development Tools"`
> $ `sudo yum install -y git libX11-devel libXft-devel libXinerama-devel`

### Install X Window System and DWM

DWM is an efficient, light-weight window manager.

> $ `git clone git://suckless.org/dwm /tmp/dwm/`
> $ `cd /tmp/dwm`
> $ `cp config.def.h config.h`
> $ `sudo make && sudo make install`
> $ `cd /tmp`
> $ `git clone http://git.
suckless.org/st ./st/
> $ `cd st`
> $ `cp config.def.g config.h`
> $ `sudo make && sudo make install`

Then edit or create `$HOME/.xinitrc` so that it has the `x` (executable) bit set and contains the lines:

> exec dwm

### Install VBoxGuestAdditions

> $ `cd /tmp`
> $ `sudo rpm -Uvh http://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm`
> $ `sudo yum install dkms`

Now insert the VBoxGuestAdditions CDROM and continue with:

> $ `sudo mount /dev/cdrom /mnt`
> $ `cd /mnt`
> $ `sudo ./VBoxLinuxAdditions.run`

run, `startx` and you're off with a basic window manager, GUI support and Git

Part 2: Setup Tools
-------------------

The tools I like to have installed are:

### Emacs with the Markdown plugin ###

Emacs is a simple terminal text editor that I prefer to tools like vim or nano.  To install it, use:
> $ sudo yum install -y emacs.x86_64 emacs-git.noarch
  
Then install the Melpa package manager so that you can get the additional Emacs Lisp plugins.  Edit or create `~/.emacs` and ensure the following commands are present:

> (require 'package)
> (add-to-list 'package-archives
>		 '("melpa" . "http://melpa.org/packages/") t)
> (package-initialize)

And open Emacs.  Enter `M-x package-list-packages` then find `markdown-mode` and install it

### Firefox ###

Chromium doesn't appear to run well under CentOS, so we install Firefox instead.  `$ sudo yum install -y firefox.x86_64`

### Configure Git ###

Set global settings

> $ git config --global user.name "Jason Hamilton"
> $ git config --global user.email "kvorak@gmail.com"

Part 3: Moving Forward
----------------------

From here, you have a very basic CentOS 7 virtual machine that is set up with a window manager, custom terminal editor and other basic tools.  The next steps involve getting the system set up to perform specific tasks and for that, you are referred to the documents below:

- [Python Development](/Setups/Python) explains how to go from this base to a functional python development environment


Caveats
-------

If an attempt to run `yum update` fails saying that it cannot find a baseurl for one of the repositories, try fixing it by running `dhclient` to reinitialize the network interface.

If `startx` complains about fonts, try to  `yum install xorg-x11-fonts-misc`
