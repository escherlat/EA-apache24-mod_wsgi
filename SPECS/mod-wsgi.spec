Name: ea-apache24-mod_wsgi
Version: 4.5.7
Summary: A WSGI compliant interface for hosting Python based web applications on top of the Apache web server
Release: 1%{?dist}
License: Apache License, Version 2.0
Group: System Environment/Daemons
URL: http://modwsgi.org
Source: https://github.com/GrahamDumpleton/mod_wsgi/archive/4.5.7.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: ea-apache24-devel
BuildRequires: python-devel
Requires: ea-apache24
Requires: python

%description
A WSGI compliant interface for hosting Python based web applications on top of the Apache web server

%prep
%setup
%{__cat} <<EOF > mod_wsgi.conf
### Load the module
LoadModule wsgi_module modules/mod_wsgi.so

EOF


%build
%configure
make %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%make_install

%clean
%{__rm} -rf %{buildroot}

%files
%{_sysconfdir}/apache2/modules/mod_wsgi.so
%config(noreplace) %{_sysconfdir}/apache2/conf.d/mod_wsgi.conf

%changelog
* Thu Sep 15 2016 Kenneth Power <kenneth.power@gmail.com> - 0.0.1
- Initial spec file creation.
EOF
