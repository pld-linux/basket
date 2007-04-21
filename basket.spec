Summary:	A container for various types of data
Summary(pl.UTF-8):	Pojemnik na różne rodzaje danych
Name:		basket
Version:	1.0.2
Release:	1
License:	GPL
Group:		Applications
# from	http://basket.kde.org/downloads/?file=%{name}-%{version}.tar.gz
Source0:	http://basket.kde.org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	d71c62a56de9cc32ba2633e63e99071f
Patch0:		%{name}-am.patch
Patch1:		kde-ac260-lt.patch
URL:		http://basket.kde.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gpgme-devel
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	kdepim-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
#BuildRequires:	unsermake >= 040805
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This application provide as many baskets (drawers) as you wish, and
you can drag and drop various objects (text, URLs, images, sounds...)
into its. Objects can be edited, copied, dragged... So, you can
arrange them as you want! This application can be used to quickly drop
web objects (link, text, images...) or notes (texts or images and,
later, sound), as well as free your clutered desktop (if any).

%description -l pl.UTF-8
Ta aplikacja udostępnia dowolną liczbę koszyków (szuflad) i pozwala
przeciągać i upuszczać na nie różne obiekty (tekst, URL-e, obrazki,
dźwięki...). Obiekty mogą być modyfikowane, kopiowane, przeciągane...
Można je układać jak tylko chcemy. Ta aplikacja może być używana do
szybkiego upuszczania obiektów WWW (odnośników, tekstu, obrazków...)
lub notatek (tekstów albo obrazków, później dźwięków), a także
uwalniania pulpitu ze śmieci.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%{__sed} -i -e 's,\$(TOPSUBDIRS),doc po src,'  Makefile.am

%build
cp -f /usr/share/automake/config.* admin
%{__make} -f admin/Makefile.common cvs

%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT%{_desktopdir}
mv $RPM_BUILD_ROOT{%{_datadir}/applnk/Utilities/basket.desktop,%{_desktopdir}}
echo "Categories=Qt;KDE;Utility;" >> $RPM_BUILD_ROOT%{_desktopdir}/basket.desktop

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libbasketcommon.so
%attr(755,root,root) %{_libdir}/kde3/kcm_basket.so
%attr(755,root,root) %{_libdir}/kde3/libbasketpart.so
%{_libdir}/kde3/libbasketpart.la
%{_libdir}/kde3/kcm_basket.la
%{_libdir}/libbasketcommon.la
%{_datadir}/apps/basket
%{_datadir}/services/basket_config_apps.desktop
%{_datadir}/services/basket_config_baskets.desktop
%{_datadir}/services/basket_config_features.desktop
%{_datadir}/services/basket_config_general.desktop
%{_datadir}/services/basket_config_notes.desktop
%{_datadir}/services/basket_config_new_notes.desktop
%{_datadir}/services/basket_config_notes_appearance.desktop
%{_datadir}/services/basket_part.desktop
%{_iconsdir}/crystalsvg/*x*/*/*.png
%{_iconsdir}/crystalsvg/scalable/apps/*.svg
%{_desktopdir}/*.desktop
