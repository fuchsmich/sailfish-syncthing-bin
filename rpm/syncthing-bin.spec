%define binname syncthing
Name:		%{binname}-bin
# Epoch:		1
Version:	0.14.39
Release:		1
Summary:	Open Source Continuous Replication / Cluster Synchronization Thing
License:	MPLv2
Group:		Applications/System
URL:		https://syncthing.net/

%define arm_basename %{binname}-linux-arm-v%{version}
%define i486_basename %{binname}-linux-386-v%{version}
%define remote_url https://github.com/syncthing/%{binname}/releases/download/v%{version}/
%define __os_install_post %{nil}

%ifarch armv7hl
	%define basenam %{arm_basename}
	%define tgz %{basenam}.tar.gz
%endif

%ifarch i486
	%define basenam %{i486_basename}
	%define tgz %{basenam}.tar.gz
%endif
Source0: 	%{tgz}
Source1:    %{binname}.service
Source2:    %{binname}@.service
Source3:    %{binname}-resume.service

# BuildRequires: go
# BuildRequires: git

#Requires(pre):     
Requires(post):    	systemd
#Requires(preun):   	systemd
#Requires(postun): 	systemd
Provides: syncthing

%description
Syncthing replaces proprietary sync and cloud services with something open, trustworthy and decentralized. Your data is your data alone and you deserve to choose where it is stored, if it is shared with some third party and how it's transmitted over the Internet.

%prep
#Why is prep not run????
echo Prep
#%setup -q

%build 
cd rpm
curl -L -O %{remote_url}%{basenam}.tar.gz

%install
export DONT_STRIP=1

rm -rf %{basenam}
tar -xzf %{SOURCE0}
install -p -D -m 0755 %{basenam}/%{binname} $RPM_BUILD_ROOT%{_bindir}/%{binname}
# install -p -D -m 0644 %{basenam}/etc/linux-systemd/user/%{binname}.service $RPM_BUILD_ROOT%{_userunitdir}/%{binname}.service
# install -p -D -m 0644 %{basenam}/etc/linux-systemd/system/%{binname}@.service $RPM_BUILD_ROOT%{_unitdir}/%{binname}@.service
install -p -D -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_userunitdir}/%{binname}.service
install -p -D -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_unitdir}/%{binname}@.service
install -p -D -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_unitdir}/%{binname}-resume.service
install -p -D -m 0644 %{basenam}/AUTHORS.txt %{basenam}/LICENSE.txt %{basenam}/README.txt .

%post
%systemd_postun  #calls systemctl daemon-reload


%files
%doc AUTHORS.txt LICENSE.txt README.txt
%{_bindir}/%{binname}
%{_userunitdir}/%{binname}.service
%{_unitdir}/%{binname}@.service
%{_unitdir}/%{binname}-resume.service

