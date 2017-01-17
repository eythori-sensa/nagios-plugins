%define debug_package %{nil}

Summary:	A Nagios plugin to report os version from /etc/os-release mainly for Reporting purposes
Name:		nagios-okplugin-check_os_version
Version:	1.0.0
Release:	1%{?dist}
License:	GPLv2+
Group:		Applications/System
URL:		https://github.com/opinkerfi/nagios-plugins
Source0:	https://github.com/opinkerfi/nagios-plugins/check_os_version/releases/nagios-okplugin-check_os_version-%{version}.tar.gz
Requires:	nagios-nrpe
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Packager:	Eythor Ivarsson <eythori@sensa.is>



%description
A Nagios plugin to report os version from /etc/os-release mainly for Reporting purposes


%prep
%setup -q
perl -pi -e "s|/usr/lib|%{_libdir}|g" nrpe.d/check_os_version.cfg

%build


%install
rm -rf %{buildroot}
install -D -p -m 0755 nrpe.d/check_os_version.cfg %{buildroot}/etc/nrpe.d/check_os_version.cfg


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
#%doc README LICENSE
/etc/nrpe.d/check_os_version.cfg

%changelog
* Tue Jan 17 2017  Eythor Ivarsson <eythori@sensa.is> 1.0.0-1
- Initial packaging
