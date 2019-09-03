<?php

class ExtendedPDO {
	
	private static $instance;

	// Tries to connect to DataBase. If not successfull throws an exception.
	public static function getInstance()
	{
		if (null === self::$instance) {
			try {
				self::$instance = new PDO('mysql:host=127.0.0.1;dbname=dbname', 'root', '');
			} catch (PDOException $e) {
				die($e->getMessage());
			}
		}

		return self::$instance;
	}

	public function fetchAll($query)
	{
		$statement = self::getInstance()->prepare($query);
		$statement->execute();

		return $statement->fetchAll(PDO::FETCH_OBJ);
	}
}