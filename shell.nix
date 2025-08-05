{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
  packages = with pkgs.python313Packages; [
    tkinter        
  ];

shellHook = ''
    python3 main.py
  '';
}