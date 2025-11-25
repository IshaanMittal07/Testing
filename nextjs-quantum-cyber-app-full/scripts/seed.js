require('dotenv').config()
const { MongoClient } = require('mongodb')

async function seed(){
 const uri=process.env.MONGODB_URI
 const client=new MongoClient(uri)
 await client.connect()
 const db=client.db(process.env.MONGODB_DB||'quantum-cyber')
 const col=db.collection('articles')
 await col.deleteMany({})
 await col.insertMany([
  {title:'Introduction to Quantum Computing',tags:['quantum','basics'],summary:'A lightweight introduction.',content:'Quantum computing...',createdAt:new Date()},
  {title:'Post-Quantum Cryptography: What to know',tags:['crypto','cybersecurity'],summary:'Overview...',content:'Post-quantum...',createdAt:new Date()}
 ])
 await client.close()
}
seed()
