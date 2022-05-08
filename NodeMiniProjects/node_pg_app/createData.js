const { pool } = require("./db");

async function insertData() {
  const [name, age] = process.argv.slice(2);
  try{
    const res =  await pool.query(
        "INSERT INTO table1 (name,age) VALUES ($1,$2);",[name,age]
    );
    console.log(`Added a row with the name ${name}`);
  } catch(error){
      console.log(error);
  }
}

insertData();