Write-Output "Ada file Java pada direktori" 

$Data = Get-ChildItem -Include *.Java* -Recurse

Write-Output $Data

<# Get-Date #>

<# Read-Host -Prompt 'Input the user name' #>

<# $Data = Read-Host -Prompt 'Input the user name' #>

If ($Data  -eq $Data)  {
	$gantiNama = Read-Host -Prompt 'Diganti namanya y / t'
	If ($gantiNama  -eq "y")  {
		$namaBaru = Read-Host -Prompt 'Input nama baru'
		Write-Output $namaBaru
		
	}
 
  } Elseif ($gantiNama  -eq "t")  {
		Write-Output "Lanjut ke process selanjutnya"

} 
