Name:    woof
Version: 0.1.0
Release: 1%{?dist}
Summary: Dog translator

License: MIT

URL:     https://github.com/nikromen/woof/
Source0: https://github.com/nikromen/woof/archive/refs/tags/%{version}.tar.gz

BuildArch: noarch

BuildRequires: python3-devel

%description
%{summary}

%prep
%autosetup -n %{name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%files
%license LISENSE
%doc README.md
%{_bindir}/hello
%{python3_sitelib}/*

%changelog
* Thu Aug 22 2022 Jiri Kyjovsky <j1.kyjovsky@gmail.com> - 0.1.0-1
- initial upstream release: 0.1.0
