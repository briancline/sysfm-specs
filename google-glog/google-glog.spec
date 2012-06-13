%define	RELEASE	1
%define rel     %{?CUSTOM_RELEASE} %{!?CUSTOM_RELEASE:%RELEASE}
%define	prefix	/usr

Name: google-glog
Summary: A C++ application logging library
Version: 0.3.2
Release: %rel
Group: Development/Libraries
URL: http://code.google.com/p/google-glog
License: BSD
Vendor: Google
Packager: Google Inc. <opensource@google.com>
Source: http://%{name}.googlecode.com/files/%{name}-%{version}.tar.gz
Distribution: Redhat 7 and above.
Buildroot: %{_tmppath}/%{name}-root
Prefix: %prefix

%description
The %name package contains a library that implements application-level
logging.  This library provides logging APIs based on C++-style
streams and various helper macros.

%package devel
Summary: A C++ application logging library
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
The %name-devel package contains static and debug libraries and header
files for developing applications that use the %name package.

%prep
%setup -n glog-%{version}

%build
./configure
make prefix=%prefix

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT%{prefix} install
mv $RPM_BUILD_ROOT%{prefix}/share/doc/glog-%{version} $RPM_BUILD_ROOT%{prefix}/share/doc/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)

## Mark all installed files within /usr/share/doc/{package name} as
## documentation.  This depends on the following two lines appearing in
## Makefile.am:
##     docdir = $(prefix)/share/doc/$(PACKAGE)-$(VERSION)
##     dist_doc_DATA = AUTHORS COPYING ChangeLog INSTALL NEWS README
%docdir %{prefix}/share/doc/%{name}-%{version}
%{prefix}/share/doc/%{name}-%{version}/*

%{prefix}/lib/libglog.so.0
%{prefix}/lib/libglog.so.0.0.0

%files devel
%defattr(-,root,root)

%{prefix}/include/glog
%{prefix}/lib/libglog.a
%{prefix}/lib/libglog.la
%{prefix}/lib/libglog.so
%{prefix}/lib/pkgconfig/libglog.pc

%changelog
    * Wed Mar 26 2008 <opensource@google.com>
    - First draft

