function [thres,location,BW_renyi] = renyi_seg_fn(im,alpha,minpv,maxpv,offset)
    [counts1, x] = imhist(im);
    p = counts1./sum(counts1);
    cp = cumsum(p);


    [r, ~, ~] = find(x > minpv & x < maxpv);
    minr = min(r);
    maxr = max(r);
    scalar = 1/(1-alpha);
    rr = maxr-minr;
    h1 = zeros(rr,1);
    h2 = zeros(rr,1);
    for ii = 1:rr
        iidash = ii+minr;
        h1(ii) = log(sum((p(1:iidash)./cp(iidash)).^alpha)+eps);
        h2(ii) = log(sum((p(iidash+1:256)./(1-cp(iidash))).^alpha)+eps);    
    end
    T = h1 + h2;

    T = T.*scalar;
    %plot(T)
    [~, indx] = max(T);
    location = indx + minr+offset;
    thres = x(location);
    BW_renyi = zeros(size(im));
    BW_renyi(im>thres) = 1;
