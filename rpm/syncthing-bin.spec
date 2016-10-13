Name:		syncthing-bin
# Epoch:		1
Version:	0.14.8
Release:		1
Summary:	Open Source Continuous Replication / Cluster Synchronization Thing
License:	MPL
# Group:
URL:		https://syncthing.net/

%define arm_basename syncthing-linux-arm-v%{version}
%define i486_basename syncthing-linux-386-v%{version}
Source0: 	%{arm_basename}.tar.gz
Source1:  	%{i486_basename}.tar.gz
Source2:  	syncthing.service

# BuildRequires: go
# BuildRequires: git

#Requires(pre):     shadow-utils
Requires(post):    	systemd
Requires(preun):   	systemd
Requires(postun): 	systemd

%description
Syncthing replaces proprietary sync and cloud services with something open, trustworthy and decentralized. Your data is your data alone and you deserve to choose where it is stored, if it is shared with some third party and how it's transmitted over the Internet.

#%prep
#echo Prep
#%setup -q

#%build 

%install
%ifarch armv7hl
rm -rf %{arm_basename}
tar -xzf %{SOURCE0}
install -p -D -m 0755 %{arm_basename}/syncthing $RPM_BUILD_ROOT%{_bindir}/syncthing
%endif
%ifarch i486
rm -rf %{i486_basename}
tar -xzf %{SOURCE1}
install -p -D -m 0755 %{i486_basename}/syncthing $RPM_BUILD_ROOT%{_bindir}/syncthing
%endif
install -p -D -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_libdir}/systemd/user/syncthing.service

%files
%{_bindir}/syncthing
%{_libdir}/systemd/user/syncthing.service