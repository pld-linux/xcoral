Summary:	Xcoral Editor
Summary(pl):    Xcoral - edytor tekstów pracuj±cy w ¶rodowisku X-ów.
Name:		xcoral
Version:	3.2
Release:	6
Copyright:	GPL
Group:		X11/Applications/Editors
Group(pl):	X11/Aplikacje/Edytory
Source:		ftp://ftp.x.org/contrib/editors/%{name}-%{version}.tar.gz
Patch0:		xcoral-misc.patch
Patch1:		xcoral-loop.patch
BuildPrereq:	XFree86-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Xcoral is a multiwindow mouse-based text editor for the XWindow System. A
built-in browser enables you to navigate through C functions, C++ classes,
methods and files.

%description -l pl
Xcoral wielookienkowy tekstowy edytor bazuj±cy na obs³udze myszki.
Posiada wbudowane mechanizmy pozwalaj±ce w sposób wyra¼ny rozgraniczyæ
tworzony tekst.

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
%configure --prefix=/usr/X11R6

make XC_LIBDIR=/usr/X11R6/share/xcoral 

%install
install -d $RPM_BUILD_ROOT/usr/X11R6/{bin,share/xcoral}

make installprefix=$RPM_BUILD_ROOT \
	XC_LIBDIR=/usr/X11R6/share/xcoral install

strip $RPM_BUILD_ROOT/usr/X11R6/bin/xcoral

gzip -9nf IAFA-PACKAGE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Doc/HTML IAFA-PACKAGE.gz
%attr(755,root,root) /usr/X11R6/bin/xcoral
/usr/X11R6/share/xcoral

%changelog
* Sat May 15 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [3.2-6]
- fixed Group(pl),
- added xcoral-{misc,loop}.patch,
- added BuildPrereq rules,
- simplifications in %install,
- added gzipping documentation,
- modified %doc section,
- cosmetic changes for common l&f,
- recompiled on rpm 3,
- package is FHS 2.0 compliant.

* Wed Jan 12 1999 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
- updating to version 3.2.

* Mon Dec 07 1998 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
- adding pl translation.

* Wed Aug  5 1998 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
- compiling with glibc2,
- added glibc patch.

* Wed Apr 29 1998 Wojciech "Sas" Ciåciwa <cieciwa@alpha.zarz.agh.edu.pl>
- Buildroot added
