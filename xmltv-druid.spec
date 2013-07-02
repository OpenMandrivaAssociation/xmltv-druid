Name:    xmltv-druid
Summary: A Gnome wizard to configure xmltv grabber jobs
Version: 0.4.0
Release: 6
Source: http://downloads.sourceforge.net/gshowtv/%{name}-%{version}.tar.gz
URL: http://gshowtv.sourceforge.net/xmltv-druid.html
License: GPL
Group: Graphical desktop/GNOME
BuildArch: noarch
#BuildRequires: perl-Gnome2
#BuildRequires: perl-XML-Simple
BuildRequires: desktop-file-utils
Requires: xmltv-grabbers

%description
Xmltv-druid is a very simple Gnome druid for selecting, configuring and 
scheduling a tv_grab task for XMLTV.

A tv_grab command is responsible of grabbing the tv listings from a web site.

When starting to use any XMLTV based application the most complex task is the 
configuration and setting up the cron job for the tv_grab command.

This program is designed to ease this.

%prep
%setup -q

%build
%make
										
%install
%makeinstall PREFIX=%{buildroot}%{_prefix}

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --remove-key="Encoding" \
  --add-category="X-MandrivaLinux-System-Configuration-GNOME;" \
  --dir %{buildroot}%{_datadir}/applications/ \
  %{buildroot}%{_datadir}/applications/*

%clean

%files
%doc AUTHORS copyright README
%{_bindir}/%{name}
#%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}*



%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.4.0-5mdv2010.0
+ Revision: 435154
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.4.0-4mdv2009.0
+ Revision: 262466
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.4.0-3mdv2009.0
+ Revision: 257199
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 11 2007 Guillaume Bedot <littletux@mandriva.org> 0.4.0-1mdv2008.1
+ Revision: 117288
- import xmltv-druid


* Tue Dec 11 2007 Guillaume Bedot <littletux@mandriva.org> 0.4.0-1mdv2008.1
- First package of xmltv-druid for Mandriva Linux

