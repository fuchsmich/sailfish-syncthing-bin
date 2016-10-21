%define binname syncthing
Name:		%{binname}-bin
# Epoch:		1
Version:	0.14.8
Release:		2
Summary:	Open Source Continuous Replication / Cluster Synchronization Thing
License:	MPL
Group:		Applications/System
URL:		https://syncthing.net/

%define arm_basename %{binname}-linux-arm-v%{version}
%define i486_basename %{binname}-linux-386-v%{version}
Source0: 	%{arm_basename}.tar.gz
Source1:  	%{i486_basename}.tar.gz
#Source2:  	%{binname}.service

# BuildRequires: go
# BuildRequires: git

#Requires(pre):     shadow-utils
Requires(post):    	systemd
Requires(preun):   	systemd
Requires(postun): 	systemd
Provides: syncthing

%description
Syncthing replaces proprietary sync and cloud services with something open, trustworthy and decentralized. Your data is your data alone and you deserve to choose where it is stored, if it is shared with some third party and how it's transmitted over the Internet.

#%prep
#echo Prep
#%setup -q

#%build 

%install
%ifarch armv7hl
	%define basenam %{arm_basename}
	%define tgz %{SOURCE0}
%endif

%ifarch i486
	%define basenam %{i486_basename}
	%define tgz %{SOURCE1}
%endif

rm -rf %{basenam}
tar -xzf %{tgz}
pwd
install -p -D -m 0755 %{basenam}/%{binname} $RPM_BUILD_ROOT%{_bindir}/%{binname}
install -p -D -m 0644 %{basenam}/etc/linux-systemd/user/%{binname}.service $RPM_BUILD_ROOT%{_userunitdir}/%{binname}.service
install -p -D -m 0644 %{basenam}/etc/linux-systemd/system/%{binname}@.service $RPM_BUILD_ROOT%{_unitdir}/%{binname}@.service
install -p -D -m 0644 %{basenam}/AUTHORS.txt %{basenam}/LICENSE.txt %{basenam}/README.txt .

%post
%systemd_postun  #calls systemctl daemon-reload


%files
%doc AUTHORS.txt LICENSE.txt README.txt
%{_bindir}/%{binname}
%{_unitdir}/%{binname}@.service
%{_userunitdir}/%{binname}.service
