%define	module	casuarius
%define name	python-%{module}
%define version 1.0
%define	rel	1
%if %mdkversion < 201100
%define release %mkrel %{rel}
%else
%define	release %{rel}
%endif

Summary:	Cython bindings for the Cassowary constraint solver
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/c/%{module}/%{module}-%{version}.tar.gz
License:	LGPLv2.1
Group:		Development/Python
Url:		https://github.com/enthought/casuarius/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	python-cython >= 0.15.1
BuildRequires:	python-devel

%description
Casuarius is a Cython wrapper for the Cassowary incremental constraint solver.

%prep
%setup -q -n %{module}-%{version}

%build
%__python setup.py build

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING.LGPL LICENSE README.rst
%py_platsitedir/%{module}*
