Name:		syncthing-bin
# Epoch:		1
Version:	0.14.7
Release:		1
Summary:	Open Source Continuous Replication / Cluster Synchronization Thing
License:	MPL
# Group:
URL:		https://syncthing.net/

#Source0: 	https://github.com/syncthing/syncthing/releases/download/v%{version}/syncthing-linux-arm-v%{version}.tar.gz
Source1:  	syncthing.service
Source2:  	arm
Source3:  	i386

# BuildRequires: go
# BuildRequires: git

#Requires(pre):     shadow-utils
Requires(post):    	systemd
Requires(preun):   	systemd
Requires(postun): 	systemd

%description
Syncthing replaces proprietary sync and cloud services with something open, trustworthy and decentralized. Your data is your data alone and you deserve to choose where it is stored, if it is shared with some third party and how it's transmitted over the Internet.

%install
echo %{_arch}
%ifarch armv7hl
echo "The arch is armv7hl"
install -p -D -m 0755 %{SOURCE2}/syncthing $RPM_BUILD_ROOT%{_bindir}/syncthing
%endif
%ifarch i486
echo "The arch is i486"
install -p -D -m 0755 %{SOURCE3}/syncthing $RPM_BUILD_ROOT%{_bindir}/syncthing
%endif
install -p -D -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_libdir}/systemd/user/syncthing.service

%files
%{_bindir}/%{name}
%{_libdir}/systemd/user/syncthing.service