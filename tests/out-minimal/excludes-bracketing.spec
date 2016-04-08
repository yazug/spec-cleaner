#
# spec file for package excludes-bracketing
#
# Copyright (c) 2013 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%bcond_with[^\s]*
%aarch64
%add_maven_depmap
%arm
%attr(\s*\([^)]*\))?

%build

%changelog
%check
%cmake
%cmake_[^\s]*
%config(\s*\([^)]*\))?
%configure
%create_exclude_filelist
%ctest
%defattr(\s*\([^)]*\))?
%define
%defined

%description
%desktop_database_post[^\s]*
%dir
%doc
%docdir
%else
%endif
%exclude
%fdupes

%files

%files_fontsconf_file
%fillup_[^\s]*
%find_gconf_schemas
%find_lang
%gem_install
%gem_packages
%ghc_fix_dynamic_rpath
%ghost
%glib2_gsettings_schema_[^\s]*

%global
%gpg_verify
%icon_theme_cache_post[^\s]*
%if(\s*\(.*)?
%ifarch
%ifnarch
%include
%insserv_[^\s]*

%install
%install_info
%install_info_delete
%ix86
%jar
%java
%javac
%jpackage_script
%kde_post_install
%kde4_makeinstall
%kernel_module_package
%kf5_makeinstall
%lang_package
%lang(\s*\([^)]*\))
%make_build
%make_install
%make_jobs
%makeinstall
%mime_database_post[^\s]*
%nagios_command_user_group_add
%nagios_user_group_add
%__os_install_post

%package
%patch[0-9]*
%perl_gen_filelist
%perl_make_install
%perl_process_[^\s]*
%pom_add_dep
%pom_remove_dep

%post
%posttrans
%postun
%pre

%prep
%pretrans
%preun
%py_compile
%qmake
%qmake5
%reconfigure_fonts_[^\s]*
%requires_[^\s]*
%restart_on_update
%run_permissions
%set_permissions
%setup
%sparc
%stop_on_removal
%suse_kernel_module_package
%suse_update_desktop_file
%systemd_preun
%systemd_requires
%tmpfiles_create
%triggerin
%triggerpostun
%triggerun
%udev_rules_update
%undefine
%verify[^\s]*
%verify(\s*\([^)]*\))?
%with
%without

%changelog
