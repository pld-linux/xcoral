Summary:	Xcoral Editor
Summary(pl):    Xcoral - edytor tekstów pracuj±cy w ¶rodowisku X-ów.
Name:		xcoral
Version:	3.2
Release:	1
Copyright:	GPL
Group:		X11/Applications/Editors
Group(pl):	X11/Aplikacje/Edycja
Source:		ftp://ftp.x.org/contrib/editors/xcoral-%{PACKAGE_VERSION}.tar.gz
BuildRoot:	/tmp/%name-%version-root

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

%build
%configure --prefix=/usr/X11R6
make XC_LIBDIR=/usr/X11R6/share/xcoral 

%install
install -d  $RPM_BUILD_ROOT/usr/X11R6/{bin,share/xcoral}
install -s xcoral $RPM_BUILD_ROOT/usr/X11R6/bin
for i in SmacLib/DEPEND SmacLib/README SmacLib/hanoi.sc SmacLib/cmd.sc\
 SmacLib/color.sc SmacLib/comments.sc SmacLib/compare-win.sc\
 SmacLib/complete-word.sc SmacLib/describe.sc SmacLib/edir.sc\
 SmacLib/edt.sc SmacLib/example.sc SmacLib/french.sc SmacLib/hack-filename.sc\
 SmacLib/head.sc SmacLib/html.sc SmacLib/java.sc SmacLib/keydef-ext.sc\
 SmacLib/latex-macros.sc SmacLib/latex.sc SmacLib/man.dtex\
 SmacLib/misc-commands.sc SmacLib/mode-ext.sc SmacLib/mode.sc\
 SmacLib/mouse.sc SmacLib/rcs.sc SmacLib/save.sc SmacLib/sun-keydef.sc\
 SmacLib/title.sc SmacLib/top-ten.sc SmacLib/utilities.sc SmacLib/version.sc\
 SmacLib/window-utilities.sc SmacLib/xcoralrc.lf; do \
(install  $i $RPM_BUILD_ROOT/usr/X11R6/share/xcoral );\
done

%files
%defattr(644, root, root, 755)
%doc Doc/* README
/usr/X11R6/share/xcoral
%attr(755, root, root)/usr/X11R6/bin/xcoral

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_DIR/%name-%version

%changelog
* Wed Jan 12 1999 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
- updating to version 3.2.

* Mon Dec 07 1998 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
- adding pl translation.

* Wed Aug  5 1998 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
- compiling with glibc2,
- added glibc patch.

* Wed Apr 29 1998 Wojciech "Sas" Ciåciwa <cieciwa@alpha.zarz.agh.edu.pl>
- Buildroot added
