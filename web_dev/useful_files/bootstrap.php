<?php 

class Bootstrap {
	// Create an array with all the files needed for the project
	private $includes = [
		'path/to/file.php',
		'path/to/file2.php',
	];

	// Function tries to require all files described in private $includes, so they
	// can be used in workspace. If files doesn't exist, throws an exception.
	public static function bootstrap()
	{
		foreach ($this->includes as $file) {
			if (file_exists($file)) {
				require_once $file;
			} else {
				throw new Exception('Tried to include file '.$file.', which doesn\'t exist.');
			}
		}
	}
}