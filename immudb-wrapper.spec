%global modname immudb_wrapper

Name:           python-%{modname}
Version:        0.1.6
Release:        1%{?dist}
Summary:        AlmaLinux immudb wrapper for Python

License:        Apache-2.0
URL:            https://github.com/AlmaLinux/immudb-wrapper
Source0:        https://github.com/AlmaLinux/immudb-wrapper/archive/refs/tags/%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
BuildRequires:  pyproject-rpm-macros

%package -n python%{python3_pkgversion}-%{modname}
Summary:            %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modname}}
Requires:       python3-immudb = 1.5.0

%description -n python%{python3_pkgversion}-%{modname}
%{summary}.
Python %{python3_pkgversion} version.

%generate_buildrequires
%pyproject_buildrequires

%description
%{summary}.

%prep
%autosetup -n %{modname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

%files -n python3-%{modname} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
* Mon May 12 2025 Eduard Abdullin <eabdullin@almalinux.org> - 0.1.6-1
- Initial release
