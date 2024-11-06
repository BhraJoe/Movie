


from django.urls import path
from .views import * 

urlpatterns = [
    
    
    
    path('', ShowHome, name='Home'),
    path('about/',ShowAbout, name='about'),
    path('contact/',ShowContact, name='contact'),
    path('services/',ShowServices, name='services'),
    path('team/',ShowTeam, name='team'),
    path('director/',Director, name='director'),
    path('mo/',Mo, name='mo'),
    path('latest/',Latest, name='latest'),
    path('movie/',Movie, name='movie'),
    path('popular/',Popular, name='popular'),
    path('up/',Up, name='up'),
    
    path('equalizer/',Equalizer, name='equalizer'),
    path('hours/',hours, name='hours'),
    path('bad/',bad, name='bad'),
    path('bade/',bade, name='bade'),
    path('beacon23/',beacon23, name='beacon23'),
    path('blood/',blood, name='blood'),
    path('breaking/',breaking, name='breaking'),
    path('breathe/',breathe, name='breathe'),
    path('bridgerton/',bridgerton, name='bridgerton'),
    path('chief/',chief, name='chief'),
    path('cleaning/',cleaning, name='cleaning'),
    path('control/',control, name='control'),
    path('darkmatter/',darkmatter, name='darkmatter'),
    path('damaged/',damaged, name='up'),
    path('dead/',dead, name='dead'),
    path('di/',di, name='di'),
    path('doctor/',doctor, name='doctor'),
    path('fallout/',fallout, name='fallout'),
    path('game/',game, name='game'),
    path('ghostbusters/',ghostbusters, name='ghostbusters'),
    path('halo/',halo, name='halo'),
    path('hangman/',hangman, name='hangman'),
    path('hotel/',hotel, name='hotel'),
    path('house/',house, name='house'),
    path('how/',how, name='how'),
    path('humane/',humane, name='humane'),
    path('interview/',interview, name='interview'),
    path('into/',into, name='into'),
    path('kill/',kill, name='kill'),
    path('landofbad/',landofbad, name='landofbad'),
    path('life/',life, name='life'),
    path('uplogan/',logan, name='logan'),
    path('madmax/',madmax, name='madmax'),
    path('mad/',mad, name='mad'),
    path('madamweb/',madamweb, name='madamweb'),
    path('mayor/',mayor, name='mayor'),
    path('neugdaesanyang/',neugdaesanyang, name='neugdaesanyang'),
    path('panggonanwingit/',panggonanwingit, name='panggonanwingit'),
    path('paradox/',paradox, name='paradox'),
    path('parasyte/',parasyte, name='parasyte'),
    path('parish/',parish, name='parish'),
    path('premsumed/',premsumed, name='premsumed'),
    path('rebel/',rebel, name='rebel'),
    path('rise/',rise, name='rise'),
    path('see/',see, name='see'),
    path('seolgyeja/',seolgyeja, name='seolgyeja'),
    path('severance/',severance, name='severance'),
    path('shadow/',shadow, name='shadow'),
    path('sistas/',sistas, name='sistas'),
    path('snowpiercer/',snowpiercer, name='snowpiercer'),
    path('space/',space, name='space'),
    path('stalked/',stalked, name='stalked'),
    path('strangers/',strangers, name='strangers'),
    path('supacall/',supacall, name='supacall'),
    path('superman/',superman, name='superman'),
    path('sweet/',sweet, name='sweet'),
    path('theacolyte/',theacolyte, name='theacolyte'),
    path('theark/',theark, name='theark'),
    path('theblacklist/',theblacklist, name='theblacklist'),
    path('theman/',theman, name='theman'),
    path('the/',the, name='the'),
    path('they/',they, name='they'),
    path('todos/',todos, name='todos'),
    path('vikings/',vikings, name='vikings'),
    path('warchief/',warchief, name='warchief'),
    path('wild/',wild, name='wild')
    


]