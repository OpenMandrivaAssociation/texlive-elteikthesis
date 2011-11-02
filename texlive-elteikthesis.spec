Name:		texlive-elteikthesis
Version:	1.2
Release:	1
Summary:	Thesis class for ELTE University Informatics wing
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/elteikthesis
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/elteikthesis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/elteikthesis.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/elteikthesis.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This is not an official University class, and has not been
approved by the University.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/elteikthesis/elteikthesis.cls
%doc %{_texmfdistdir}/doc/latex/elteikthesis/README
%doc %{_texmfdistdir}/doc/latex/elteikthesis/elteikthesis.pdf
%doc %{_texmfdistdir}/doc/latex/elteikthesis/example.pdf
%doc %{_texmfdistdir}/doc/latex/elteikthesis/example.tex
%doc %{_texmfdistdir}/doc/latex/elteikthesis/pics/eltecimerszines.eps
%doc %{_texmfdistdir}/doc/latex/elteikthesis/pics/eltecimerszines.jpg
#- source
%doc %{_texmfdistdir}/source/latex/elteikthesis/elteikthesis.dtx
%doc %{_texmfdistdir}/source/latex/elteikthesis/elteikthesis.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
