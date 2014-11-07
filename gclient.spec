%define		svnrev	72
%define		rel	2
Summary:	Wrapper script for checking out and updating source code from multiple SCM repository locations
Name:		gclient
Version:	0.3.1
Release:	0.%{svnrev}.%{rel}
License:	Apache v2.0
Group:		Applications/System
# svn co http://gclient.googlecode.com/svn/trunk/gclient gclient
# tar -cjf gclient-$(svnversion gclient).tar.bz2 --exclude=.svn --remove-files gclient
Source0:	%{name}-%{svnrev}.tar.bz2
# Source0-md5:	7c127053cb66669d291194b6e990acf5
URL:		http://code.google.com/p/gclient/
Requires:	python
Requires:	python-modules
Requires:	python-mox
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

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p gclient.py $RPM_BUILD_ROOT%{_bindir}/gclient

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_bindir}/gclient
