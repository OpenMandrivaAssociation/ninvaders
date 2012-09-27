Name:		ninvaders
Version:	0.1.1
Release:	%mkrel 2
Summary:	Space Invaders clone written in ncurses for cli gaming
Group:		Games/Arcade
License:	GPLv2+
URL:		http://ninvaders.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		ninvaders-0.1.1-add-debuginfo.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:	ncurses-devel

%description
Ever wanted to play space invaders when you can't find a GUI? Now you can!
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
%__install -m0755 nInvaders %{buildroot}%{_bindir}/ninvaders

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc ChangeLog README
%{_bindir}/ninvaders

