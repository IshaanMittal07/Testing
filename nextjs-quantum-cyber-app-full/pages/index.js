import Link from 'next/link'
import {useEffect,useState} from 'react'

export default function Home(){
 const [articles,setArticles]=useState([])
 const [loading,setLoading]=useState(true)
 useEffect(()=>{(async()=>{
   const r=await fetch('/api/articles'); const j=await r.json(); setArticles(j); setLoading(false);
 })()},[])
 return (<main className="container"><header className="header"><h1>{process.env.NEXT_PUBLIC_SITE_TITLE||'Quantum & Cyber'}</h1></header>
 {loading?'Loading…':articles.map(a=><div key={a._id}><Link href={'/articles/'+a._id}>{a.title}</Link></div>)}
 </main>)
}