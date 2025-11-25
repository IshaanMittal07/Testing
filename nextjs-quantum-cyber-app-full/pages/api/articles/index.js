import clientPromise from '../../../lib/mongodb'

export default async function handler(req,res){
 const client=await clientPromise
 const db=client.db(process.env.MONGODB_DB||'quantum-cyber')
 const col=db.collection('articles')
 if(req.method==='GET'){
   const docs=await col.find({}).toArray()
   res.json(docs.map(d=>({...d,_id:d._id.toString()})))
 } else if(req.method==='POST'){
   const doc={...req.body,createdAt:new Date()}
   const r=await col.insertOne(doc)
   res.status(201).json({insertedId:r.insertedId.toString()})
 } else res.status(405).end()
}
