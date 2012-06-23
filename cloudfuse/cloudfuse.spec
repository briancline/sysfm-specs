Summary:        A FUSE application which provides access to Rackspace's Cloud Files 
Name:           cloudfuse 
Version:        20120604
Release:        1%{?dist}
License:        BSD
Group:          System Environment/Libraries

Source0:        redbo-cloudfuse-2cd8214.tar.gz
URL:            http://redbo.github.com/cloudfuse/ 

BuildRequires:  curl-devel fuse fuse-devel fuse-libs libxml2 libxml2-devel openssl-devel

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


%description
Cloudfuse is a FUSE application which provides access to Rackspace's
Cloud Files (or any installation of Swift).

Cloud Files is a remote storage system which is similar in principle to
Amazon S3.  It provides a simple RESTful interface to storing and retrieving
objects.

Swift, the software behind Cloud Files, has been open-sourced as part of the
OpenStack project.

%prep
%setup -n redbo-cloudfuse-2cd8214 


%build
./configure
make 


%install
rm -rf $RPM_BUILD_ROOT

install -D -p -m 755 cloudfuse $RPM_BUILD_ROOT%{_bindir}/cloudfuse


%files
%defattr(-,root,root,-)
%doc README LICENSE 
%{_bindir}/cloudfuse


%clean
rm -rf $RPM_BUILD_ROOT


%changelog
* Wed Jun 20 2012 Matt <matt@claritum.com> - 20120604-1
- Initial spec file
