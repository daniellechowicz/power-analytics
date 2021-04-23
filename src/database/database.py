import sqlite3


class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = self.connect_to_database()
        self.cursor = self.connection.cursor()
        # Metadata table initialization
        try:
            self.create_metadata_table()
        except:
            print("[INFO] table metadata already exists")

        # Stats table initialization
        try:
            self.create_stats_table()
        except:
            print("[INFO] table metadata already exists")

    def connect_to_database(self):
        connection = sqlite3.connect("pkgs/src/database/{}.db".format(self.db_name))
        print(
            "[INFO] new connection {} has been opened successfully".format(connection)
        )

        return connection

    def create_metadata_table(self):
        self.connection.cursor().execute(
            """CREATE TABLE metadata(
            measurement_id INTEGER PRIMARY KEY AUTOINCREMENT,
            author TEXT,
            measurement_date TEXT NOT NULL,
            material TEXT NOT NULL,
            moisture_content INTEGER NOT NULL,
            cutting_direction TEXT NOT NULL,
            rotational_speed REAL NOT NULL,
            feed_speed REAL NOT NULL,
            feed_per_tooth REAL NOT NULL,
            cutting_speed REAL NOT NULL,
            cutting_width REAL NOT NULL,
            cutting_depth REAL NOT NULL,
            cutting_angle REAL NOT NULL,
            mean_chip_thickness REAL NOT NULL,
            mean_chip_length REAL NOT NULL,
            tool_id REAL NOT NULL,
            classification_number TEXT NOT NULL,
            strategic_business_unit TEXT NOT NULL,
            tool_diameter REAL NOT NULL,
            tool_cutting_width REAL NOT NULL,
            no_of_wings INTEGER NOT NULL,
            total_no_of_wings INTEGER NOT NULL,
            cutting_material TEXT NOT NULL,
            cutting_material_quality TEXT NOT NULL,
            body_material TEXT NOT NULL,
            n_max REAL,
            n_opt REAL,
            rake_angle REAL,
            comments TEXT)"""
        )
        self.connection.commit()
        print("[INFO] table metadata has been created successfully")

    def create_stats_table(self):
        self.cursor.execute(
            """CREATE TABLE stats(
            mean REAL NOT NULL,
            measurement_id INTEGER NOT NULL,
            FOREIGN KEY(measurement_id) REFERENCES metadata(measurement_id))"""
        )
        self.connection.commit()
        print("[INFO] table stats has been created successfully")

    def insert_into_metadata(
        self,
        author,
        measurement_date,
        material,
        moisture_content,
        cutting_direction,
        rotational_speed,
        feed_speed,
        feed_per_tooth,
        cutting_speed,
        cutting_width,
        cutting_depth,
        cutting_angle,
        mean_chip_thickness,
        mean_chip_length,
        tool_id,
        classification_number,
        strategic_business_unit,
        tool_diameter,
        tool_cutting_width,
        no_of_wings,
        total_no_of_wings,
        cutting_material,
        cutting_material_quality,
        body_material,
        n_max,
        n_opt,
        rake_angle,
        comments,
    ):
        params = (
            author,
            measurement_date,
            material,
            moisture_content,
            cutting_direction,
            rotational_speed,
            feed_speed,
            feed_per_tooth,
            cutting_speed,
            cutting_width,
            cutting_depth,
            cutting_angle,
            mean_chip_thickness,
            mean_chip_length,
            tool_id,
            classification_number,
            strategic_business_unit,
            tool_diameter,
            tool_cutting_width,
            no_of_wings,
            total_no_of_wings,
            cutting_material,
            cutting_material_quality,
            body_material,
            n_max,
            n_opt,
            rake_angle,
            comments,
        )
        self.cursor.execute(
            """INSERT INTO metadata (
            author,
            measurement_date,
            material,
            moisture_content,
            cutting_direction,
            rotational_speed,
            feed_speed,
            feed_per_tooth,
            cutting_speed,
            cutting_width,
            cutting_depth,
            cutting_angle,
            mean_chip_thickness,
            mean_chip_length,
            tool_id,
            classification_number,
            strategic_business_unit,
            tool_diameter,
            tool_cutting_width,
            no_of_wings,
            total_no_of_wings,
            cutting_material,
            cutting_material_quality,
            body_material,
            n_max,
            n_opt,
            rake_angle,
            comments) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            params,
        )
        self.connection.commit()

    def insert_into_stats(self, mean, measurement_id):
        params = (mean, measurement_id)
        self.cursor.execute(
            """INSERT INTO stats ( 
            mean, 
            measurement_id) VALUES (?, ?)""",
            params,
        )
        self.connection.commit()

    def fetch_all(self, table: str):
        results = self.cursor.execute("SELECT * FROM {}".format(table))
        for result in results.fetchall():
            print(result)

    def execute_command(self, command):
        result = self.cursor.execute(command).fetchall()

        return result

    # A script containing single line
    def execute_external_script(self, script):
        # Open and read the file as a single buffer
        fd = open(script, "r")
        command = fd.read()
        fd.close()

        result = self.cursor.execute(command).fetchall()

        return result

    # A script containing multiple lines
    def execute_external_complex_script(self, script):
        # Open and read the file as a single buffer
        fd = open(script, "r")
        sql_script = fd.read()
        fd.close()

        # All SQL commands (split on ';')
        sql_commands = sql_script.split(";")

        # Execute every command from the input file
        for command in sql_commands:
            # This will skip and report errors
            # For example, if the tables do not yet exist, this will skip over
            # the DROP TABLE commands
            try:
                self.cursor.execute(command).fetchall()
            except Exception as e:
                print("[INFO] {}".format(e))
