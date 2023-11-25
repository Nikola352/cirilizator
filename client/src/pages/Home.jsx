import React from 'react';
import Navbar from '../components/Navbar';
import Banner from '../components/Banner';
import FeatureSection from '../components/FeatureSection';
import FontTypesBanner from '../components/FontTypesBanner';
import Footer from '../components/Footer';


export default function Home() {
    
    return(
        <div>
            <Navbar />
            <Banner />
            <FontTypesBanner />
            <FeatureSection  />
            <Footer />

            
        </div>
    )
}