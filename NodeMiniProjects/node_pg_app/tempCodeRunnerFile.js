try{
        const read = await pool.query(
            "SELECT * FROM table1"
        );