Summary:	A customized configuration of the fvwm2 window manager.
Name:		AnotherLevel
Version:	0.9
Release:	1
Copyright:	distributable
Group:		X11/Window Managers
Group(de):	X11/Fenstermanager
Group(pl):	X11/Zarz±dcy Okien
Source0:	%{name}-%{version}.tar.gz
Requires:	m4, fvwm2, fvwm2-icons, wmconfig > 0.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	TheNextLevel
BuildArchitectures:	noarch

%define		_prefix	/usr/X11R6
%define		_mandir	/usr/X11R6/man

%description 
AnotherLevel is a custom configuration of the popular fvwm2 window
manager. Fvwm stands for (?) virtual window manager. You can fill in
the blank for the 'f': fast, flexible, friendly and fabulous all could
apply. This window manager is based on TheNextLevel desktop
configuration, created by Greg J. Badros, which won the 1996 Red Hat
Desktop Contest.

AnotherLevel is designed to be easily configured by the user.

%descritpion -l pl
AnotherLevel jest u¿yteczn± konfiguracj± popularnego zarz±dcy
okien, jakim jest fvwm2. Fvwm oznacza (?) wirtualnego zarz±dcê
okien. Zamiast znaku zapytania mo¿na dopisaæ:szybki, elastyczny,
przyjazny i fantastyczny - wszystko to pasowa³oby do niego. Ten
zarz±dca okien bazuje na konfiguracji pulpitu w stylu TheNextLevel 
stworzonej przez Grega J. Bradosa, która wygra³a Red Hat Desktop
Contest w 1996 roku.

%prep
%setup -c -q

%build
echo "No build necessary"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install TOPDIR=$RPM_BUILD_ROOT \
	ICONDIR=%{_datadir}/icons \
	MANDIR=%{_mandir}/man1

install -d $RPM_BUILD_ROOT%{_sysconfdir}/X11/TheNextLevel
ln -sf ../AnotherLevel/fvwm2rc.m4 \
$RPM_BUILD_ROOT%{_sysconfdir}/X11/TheNextLevel/.fvwm2rc.m4

install -d $RPM_BUILD_ROOT%{_sysconfdir}/X11/gdm/Sessions
install AnotherLevel.session \
$RPM_BUILD_ROOT%{_sysconfdir}/X11/gdm/Sessions/AnotherLevel

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Sample.Xmodmap
%dir %{_sysconfdir}/X11/AnotherLevel
%config %{_sysconfdir}/X11/AnotherLevel/*
%{_sysconfdir}/X11/TheNextLevel
%attr(755,root,root) %{_sysconfdir}/X11/gdm/Sessions/AnotherLevel
%{_datadir}/icons/*.xpm
%{_datadir}/icons/mini/*.xpm
%{_mandir}/man1/*
%attr(755,root,root) %{_bindir}/*
