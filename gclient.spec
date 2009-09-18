%define	snap	20090918
Summary:	Wrapper script for checking out and updating source code from multiple SCM repository locations
Name:		gclient
Version:	0.1
Release:	0.%{snap}.1
License:	Apache
Group:		Applications/System
# svn export http://gclient.googlecode.com/svn/trunk/ gclient
Source0:	%{name}-%{snap}.tar.bz2
# Source0-md5:	a06187007c1209d43d88fe5ade8d768a
URL:		http://code.google.com/p/gclient/
Requires:	python
Requires:	python-modules
Requires:	python-pymox
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The gclient script manages checkouts and updates for a set of client
modules in various SCM repository locations.

The gclient script currently handles basic management of one or more
Subversion modules, along with their dependent modules. Module sources
may exist in separate, different Subversion repositories. Addition of
other SCM systems is planned.

%prep
%setup -q -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install gclient.py $RPM_BUILD_ROOT%{_bindir}/gclient

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_bindir}/gclient
