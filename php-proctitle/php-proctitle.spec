%define modname proctitle
%global php_apiver  %((echo 0; php -i 2>/dev/null | sed -n 's/^PHP API => //p') | tail -1)
%global php_extdir  %(php-config --extension-dir 2>/dev/null || echo "undefined")
%global php_version %(php-config --version 2>/dev/null || echo 0)


Name:		php-proctitle
Version:	0.1.2
Release:	1%{?dist}
Summary:	Allows setting the current process name on Linux and BSD.

Group:		Development/Languages
License:	PHP
URL:		http://pecl.php.net/package/%{modname}
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	php-devel
Requires:	php(zend-abi) = %{php_zend_api}
Requires:	php(api) = %{php_apiver}


%description
This extension allows changing the current process’ name on Linux and *BSD systems. This is useful when using pcntl_fork() to identify running processes in process list.


%prep
%setup -q -c 

cat > %{modname}.ini << 'EOF'
extension=%{modname}.so
EOF


%build
cd %{modname}-%{version}
%{_bindir}/phpize
%configure
%{__make} %{?_smp_mflags}


%install
pushd %{modname}-%{version}
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} install INSTALL_ROOT=$RPM_BUILD_ROOT
popd
install -Dpm 644 %{modname}.ini %{buildroot}%{_sysconfdir}/php.d/%{modname}.ini


%clean
%{__rm} -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc %{modname}-%{version}/LICENSE %{modname}-%{version}/README
#package*.xml
%config(noreplace) %{_sysconfdir}/php.d/%{modname}.ini
%{php_extdir}/%{modname}.so



%changelog

