Name:		sysfm-release
Version:	6
Release:	1%{?dist}
Summary:	sys.fm enterprise linux repository configuration

Group:		System Environment/Base
License:	BSD
URL:		http://rpm.sys.fm
Source0:	sysfm.repo
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArchitectures: 	noarch

Requires:	yum
Requires:	redhat-release >= %{version}

%description
Provides yum repository configuration files for the sys.fm repositories.
This repo is enabled by default and does not provide signed packages, so 
no GPG keys are provided. If you wish to disable it by default unless
explicitly specified with yum, set enabled=0 in the repo file.

%global _binaries_in_noarch_packages_terminate_build 0


%prep
%setup -c -T


%build


%install
rm -rf $RPM_BUILD_ROOT
%{__install} -Dpm 644 %{SOURCE0} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/sysfm.repo


%clean
rm -rf $RPM_BUILD_ROOT


%post


%postun


%files
%defattr(-,root,root,-)
%config(noreplace) /etc/yum.repos.d/sysfm.repo


%changelog

