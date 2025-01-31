Name:		ninvaders
Version:	0.1.1
Release:	2
Summary:	Space Invaders clone written in ncurses for cli gaming
Group:		Games/Arcade
License:	GPLv2+
URL:		https://ninvaders.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		ninvaders-0.1.1-add-debuginfo.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:	ncurses-devel

%description
Ever wanted to place space invaders when you can't find a GUI? Now you can!
ninvaders is a ncurses based space invaders clone to play from the command
line.

%prep
%setup -q
%patch0 -p0

%build
%make

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_bindir}
%__install -c -m0755 nInvaders %{buildroot}%{_bindir}/ninvaders

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc ChangeLog README gpl.txt
%{_bindir}/ninvaders



%changelog
* Fri Dec 23 2011 Andrey Bondrov <abondrov@mandriva.org> 0.1.1-1mdv2011.0
+ Revision: 744857
- imported package ninvaders

