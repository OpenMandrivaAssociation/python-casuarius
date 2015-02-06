%define	module	casuarius

Summary:	Cython bindings for the Cassowary constraint solver
Name:		python-%{module}
Version:	1.1
Release:	2
Source0:	http://pypi.python.org/packages/source/c/%{module}/%{module}-%{version}.tar.gz
License:	LGPLv2.1
Group:		Development/Python
Url:		https://github.com/enthought/casuarius/
BuildRequires:	python-cython >= 0.15.1
BuildRequires:	python-devel

%description
Casuarius is a Cython wrapper for the Cassowary incremental constraint solver.

%prep
%setup -q -n %{module}-%{version}

%build
%__python setup.py build

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%files
%doc COPYING.LGPL LICENSE README.rst
%py_platsitedir/%{module}*


%changelog
* Mon Aug 13 2012 Lev Givon <lev@mandriva.org> 1.0-1
+ Revision: 814682
- imported package python-casuarius

