Summary:	A customized configuration of the fvwm2 window manager.
Name:		AnotherLevel
Version:	0.9
Release:	1
Copyright:	distributable
Group:		X11/Window Managers
Group(pl):	X11/Zarz±dcy Okien
Source:		AnotherLevel-0.9.tar.gz
Requires:	m4, fvwm2, fvwm2-icons, wmconfig > 0.3
BuildRoot:	/tmp/%{name}-%{version}-root
Obsoletes:	TheNextLevel
BuildArchitectures: noarch

%define		_prefix	/usr/X11R6
%define		_mandir	/usr/X11R6/man

%description 
AnotherLevel is a custom configuration of the popular fvwm2
window manager. Fvwm stands for (?) virtual window manager.
You can fill in the blank for the 'f': fast, flexible, 
friendly and fabulous all could apply. This window manager
is based on TheNextLevel desktop configuration, created
by Greg J. Badros, which won the 1996 Red Hat Desktop 
Contest.

AnotherLevel is designed to be easily configured by the 
user.

%prep
%setup -c -q

%build
echo "No build necessary"

%install
rm -rf $RPM_BUILD_ROOT

make install TOPDIR=$RPM_BUILD_ROOT \
	ICONDIR=%{_datadir}/icons \
	MANDIR=%{_mandir}/man1

install -d $RPM_BUILD_ROOT/etc/X11/TheNextLevel
ln -sf ../AnotherLevel/fvwm2rc.m4 \
	$RPM_BUILD_ROOT/etc/X11/TheNextLevel/.fvwm2rc.m4

install -d $RPM_BUILD_ROOT/etc/X11/gdm/Sessions
install AnotherLevel.session \
	$RPM_BUILD_ROOT/etc/X11/gdm/Sessions/AnotherLevel

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Sample.Xmodmap
%dir /etc/X11/AnotherLevel
%config /etc/X11/AnotherLevel/*
/etc/X11/TheNextLevel
%attr(755,root,root) /etc/X11/gdm/Sessions/AnotherLevel
%{_datadir}/icons/*.xpm
%{_datadir}/icons/mini/*.xpm
%{_mandir}/man1/*
%attr(755,root,root) %{_bindir}/*
