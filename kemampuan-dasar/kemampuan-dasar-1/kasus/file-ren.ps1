Write-Output "Ada file Java pada direktori"
$Data = Get-ChildItem -Include *.Java* -Recurse
Write-Output $Data

If ($Data  -eq $Data)  {
	$gantiNama = Read-Host -Prompt 'Diganti namanya y / t' 
	If ($gantiNama  -eq "y")  {
		$namaBaru = Read-Host -Prompt 'Input nama baru'
		$filebaru = $namaBaru + ".java"
		Rename-Item $Data $filebaru 
		Write-Output $filebaru
		}
}

	Elseif ($gantiNama  -eq "t")  {
		Write-Output "Lanjut ke process selanjutnya"

}
