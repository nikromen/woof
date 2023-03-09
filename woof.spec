Name:    woof
Version: 0.1.0
Release: 1%{?dist}
Summary: Dog translator

License: MIT

URL:     https://github.com/nikromen/woof/
Source0: https://github.com/nikromen/woof/archive/refs/tags/%{version}.tar.gz

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-setuptools


%description
%{summary}


%prep
%autosetup


%build
%pyproject_wheel


%install
%pyproject_install


%files
%license LICENSE
%doc README.md
%{_bindir}/woof
%{python3_sitelib}/*

%changelog
* Thu Sep 22 2022 Jiri Kyjovsky <j1.kyjovsky@gmail.com> - 0.1.0-1
- initial upstream release: 0.1.0
