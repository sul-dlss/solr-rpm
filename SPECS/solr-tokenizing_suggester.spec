%define debug_package %{nil}
%define solr_install_dir %{_javadir}/solr
%define plugin_name tokenizing_suggester

Name:           solr-%{plugin_name}
Version:        0.0.1
Release:        0%{?dist}
Summary:        A distributed, highly available, RESTful search engine

Group:          System Environment/Daemons
License:        ASL 2.0
URL:            http://lucene.apache.org/solr/
Source0:        http://archive.apache.org/dist/lucene/solr/%{version}/solr-%{version}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:       solr >= 6.6.0

Provides: %{name}

%description
A distributed, highly available, RESTful search engine

%prep
%setup -q -n solr-6.6.0

%build
true

%install
rm -rf $RPM_BUILD_ROOT

%{__mkdir} -p %{buildroot}%{solr_install_dir}/dist
%{__install} -p -m 644 dist/solr-tokenizing_suggester-*.jar %{buildroot}%{solr_install_dir}/dist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{solr_install_dir}/dist/solr-tokenizing_suggester-*.jar

%changelog
* Wed Jul 5 2017 Chris Beer <chris@cbeer.info> - 0.0.1-0
- Initial commit
