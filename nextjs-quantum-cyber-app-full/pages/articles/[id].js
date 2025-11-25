import clientPromise from '../../lib/mongodb'
import {ObjectId} from 'mongodb'

export async function getServerSideProps({params}){
 const client=await clientPromise
 const db=client.db(process.env.MONGODB_DB||'quantum-cyber')
 const a=await db.collection('articles').findOne({_id:new ObjectId(params.id)})
 if(!a) return {notFound:true}
 a._id=a._id.toString(); a.createdAt=a.createdAt.toISOString()
 return {props:{article:a}}
}
export default function ArticlePage({article}){return <main><h1>{article.title}</h1><p>{article.content}</p></main>}
