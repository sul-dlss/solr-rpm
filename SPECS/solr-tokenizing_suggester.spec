%define debug_package %{nil}
%define solr_install_dir %{_javadir}/solr
%define plugin_install_dir %{solr_install_dir}/plugins
%define plugin_name tokenizing_suggester
%define solr_version 8.0.0
%define __jar_repack 0

Name:           solr-%{plugin_name}
Version:        2.0
Release:        0%{?dist}
Summary:        A Lucene/Solr filter and filter factory to fold certain CJK characters to improve recall.

Group:          System Environment/Daemons
License:        ASL 2.0
URL:            https://github.com/sul-dlss/solr-tokenizing-suggester
Source0:        https://github.com/sul-dlss/solr-tokenizing-suggester/releases/download/v%{version}.0/tokenizing-suggest-v%{version}.jar
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       solr >= %{solr_version}

Provides: %{name}

%description
A Lucene/Solr plugin to drive content search


%install
rm -rf $RPM_BUILD_ROOT

%{__mkdir} -p %{buildroot}%{plugin_install_dir}
%{__install} -p -m 755 %{SOURCE0} %{buildroot}%{plugin_install_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{plugin_install_dir}/*

%changelog
* Wed Jul 15 2020 Chris Beer <chris@cbeer.info> - 2.0-0
- Update to v2.0
