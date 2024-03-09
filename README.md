<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>

<body>
    <h1>Mid-Point Ellipse Drawing Algorithm Rules</h1>
    <p>The original equation of the ellipse:</p>
    <p style="font-family: 'Courier New', Courier, monospace;">f(x, y) = b<sup>2</sup>x<sup>2</sup> + a<sup>2</sup>y<sup>2</sup> - a<sup>2</sup>b<sup>2</sup> = 0</p>
    <h2>Region 1:</h2>
    <ul>
        <li>Initial point: (0, b)</li>
        <li>Decision parameter: p<sub>1k</sub> = b<sup>2</sup> - a<sup>2</sup> b + 1/4 a<sup>2</sup></li>
        <li>Next point:</li>
        <ul>
            <li>If f(x, y) < 0:</li>
            <ul>
                <li>The next point will be (X<sub>k+1</sub>, y<sub>k</sub>)</li>
                <li>p<sub>1k+1</sub> = p<sub>1k</sub> + 2 b<sup>2</sup>  X<sub>k+1</sub>  + b<sup>2</sup></li>
            </ul>
            <li>Else:</li>
            <ul>
                <li>The next point will be (X<sub>k+1</sub>, y<sub>k-1</sub>)</li>
                <li>p<sub>1k+1</sub> = p<sub>1k</sub> + 2 b<sup>2</sup> X<sub>k+1</sub>  + b<sup>2</sup> - 2 a<sup>2</sup> y<sub>k+1</sub></li>
            </ul>
        </ul>
        <li>Continue until  2b<sup>2</sup> X<sub>k</sub> >= 2 a<sup>2</sup> y<sub>k</sub></li>
    </ul>
    <h2>Region 2:</h2>
    <ul>
        <li>Initial point: (Ending point of Region 1)</li>
        <li>Decision parameter: p<sub>2k</sub> = (x<sub>k</sub> + 1/2)<sup>2</sup> b<sup>2</sup> + (y<sub>k</sub> - 1)<sup>2</sup> a<sup>2</sup> - a<sup>2</sup>b<sup>2</sup></li>
        <li>Next point:</li>
        <ul>
            <li>If f(x, y) > 0:</li>
            <ul>
                <li>The next point will be (x<sub>k</sub>, y<sub>k-1</sub>)</li>
                <li>p<sub>2k+1</sub> = p<sub>2k</sub> + a<sup>2</sup> - 2 a<sup>2</sup> y<sub>k-1</sub></li>
            </ul>
            <li>Else:</li>
            <ul>
                <li>The next point will be (x<sub>k+1</sub>, y<sub>k-1</sub>)</li>
                <li>p<sub>2k+1</sub> = p<sub>2k</sub> + a<sup>2</sup> - 2 a<sup>2</sup> y<sub>k-1</sub>+ 2 b<sup>2</sup> x<sub>k+1</sub></li>
            </ul>
        </ul>
    </ul>
</body>

</html>
