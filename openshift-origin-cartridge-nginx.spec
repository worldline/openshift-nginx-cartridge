%global cartridgedir %{_libexecdir}/openshift/cartridges/nginx

Summary:       Provides Nginx support
Name:          openshift-origin-cartridge-nginx
Version:       1.0.0
Release:       1%{?dist}
Group:         Development/Languages
License:       ASL 2.0
URL:           http://www.openshift.com
Source0:       http://mirror.openshift.com/pub/openshift-origin/source/%{name}/%{name}-%{version}.tar.gz
Requires:      bc
Requires:      rubygem(openshift-origin-node)
Requires:      openshift-origin-node-util
Requires:      lsof
Provides:      openshift-origin-cartridge-nginx-1.0 = 2.0.0
Obsoletes:     openshift-origin-cartridge-nginx-1.0 <= 1.99.9
BuildArch:     noarch

%description
Provides Nginx support to OpenShift. (Cartridge Format V2)

%prep
%setup -q

%build
%__rm %{name}.spec
%__rm -rf rel-eng

%install
%__mkdir -p %{buildroot}%{cartridgedir}
%__cp -r * %{buildroot}%{cartridgedir}

%post
# To modify an alternative you should:
# - remove the previous version if it's no longer valid
# - install the new version with an increased priority
# - set the new version as the default to be safe

%files
%dir %{cartridgedir}
%attr(0755,-,-) %{cartridgedir}/bin/
%{cartridgedir}/conf
%{cartridgedir}/lib
%{cartridgedir}/metadata
%{cartridgedir}/template
%doc %{cartridgedir}/README.md
%doc %{cartridgedir}/LICENSE

%changelog
* Mon Jul 21 2014 Nicolas MESSIN <nicolas.messin@worldline.com> 1.0.0
- First version nginx cartridge openshift 4.0
