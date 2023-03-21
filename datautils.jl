# this file is automatically generated by src/stats.py.
# editing it directly is not advised.

"""
    function get_digits(digits)

Parse `digits` as an argument to a hfun function.
"""
get_digits(digits::Int) = digits
get_digits(args::Vector{String}) = parse(Int, args[1])

"""
    function parseround(value, digits)

Round `value` to `digits` digits, parsing `digits` if necessary.
"""
parseround(value, digits) = round(value; digits=get_digits(digits))

"""
    function hfun_total_anime()

Get the total anime.
"""
hfun_total_anime() = 722

"""
    function hfun_total_watching()

Get the total watching anime.
"""
hfun_total_watching() = 7

"""
    function hfun_width_total_watching()

Get the percentage watching anime takes up out of total anime.
"""
function hfun_width_watching()
    convert(Float64, 100*(hfun_total_watching()/hfun_total_anime()))
end

"""
    function hfun_total_completed()

Get the total completed anime.
"""
hfun_total_completed() = 241

"""
    function hfun_width_total_completed()

Get the percentage completed anime takes up out of total anime.
"""
function hfun_width_completed()
    convert(Float64, 100*(hfun_total_completed()/hfun_total_anime()))
end

"""
    function hfun_total_onhold()

Get the total onhold anime.
"""
hfun_total_onhold() = 3

"""
    function hfun_width_total_onhold()

Get the percentage onhold anime takes up out of total anime.
"""
function hfun_width_onhold()
    convert(Float64, 100*(hfun_total_onhold()/hfun_total_anime()))
end

"""
    function hfun_total_dropped()

Get the total dropped anime.
"""
hfun_total_dropped() = 4

"""
    function hfun_width_total_dropped()

Get the percentage dropped anime takes up out of total anime.
"""
function hfun_width_dropped()
    convert(Float64, 100*(hfun_total_dropped()/hfun_total_anime()))
end

"""
    function hfun_total_plantowatch()

Get the total plantowatch anime.
"""
hfun_total_plantowatch() = 467

"""
    function hfun_width_total_plantowatch()

Get the percentage plantowatch anime takes up out of total anime.
"""
function hfun_width_plantowatch()
    convert(Float64, 100*(hfun_total_plantowatch()/hfun_total_anime()))
end

"""
    function hfun_total_episodes()

Get the total number of episodes watched.
"""
hfun_total_episodes() = 2646

"""
    function hfun_total_rewatched()

Get the total number of episodes rewatched.
"""
hfun_total_rewatched() = 0

"""
    function hfun_score_mean(digits=3)

Get the mean score.
"""
hfun_score_mean(digits=3) = parseround(7.040650406504065, digits)

"""
    function hfun_score_var(digits=3)

Get the (uncorrected) variance of scores.
"""
hfun_score_var(digits=3) = parseround(2.494282503800648, digits)

"""
    function hfun_score_std(digits=3)

Get the (uncorrected) standard deviation of scores.
"""
hfun_score_std(digits=3) = parseround(1.5793297641090185, digits)

"""
    function hfun_score_entropy(digits=3)

Get the entropy of scores in bits
"""
hfun_score_entropy(digits=3) = parseround(2.6558735014692414, digits)
